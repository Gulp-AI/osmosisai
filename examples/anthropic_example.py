"""
Example demonstrating how to use osmosis-wrap with Anthropic
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import and initialize osmosis_wrap
import osmosis_wrap

# Initialize with Hoover API key
hoover_api_key = os.environ.get("HOOVER_API_KEY")
osmosis_wrap.init(hoover_api_key)

# Print messages to console for demonstration
osmosis_wrap.print_messages = True

print("Anthropic Integration Example\n")

try:
    # Import Anthropic after osmosis_wrap is initialized
    from anthropic import Anthropic
    
    # Get API key from environment
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    # Create the Anthropic client
    client = Anthropic(api_key=api_key)
    
    # Make a request to Claude
    print("Making request to Claude...")
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=150,
        messages=[
            {"role": "user", "content": "Hello, Claude! What are three interesting facts about neural networks?"}
        ]
    )
    
    # Print the response
    print("\nResponse from Claude:")
    print(response.content[0].text)
    
    # Example with async client (commented out by default)
    """
    print("\nAsync Client Example")
    from anthropic import AsyncAnthropic
    import asyncio
    
    async def call_claude_async():
        async_client = AsyncAnthropic(api_key=api_key)
        response = await async_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=150,
            messages=[
                {"role": "user", "content": "Hello, async Claude! What are the key differences between CNNs and RNNs?"}
            ]
        )
        print("\nAsync Response from Claude:")
        print(response.content[0].text)
        return response
    
    # Run the async example
    asyncio.run(call_claude_async())
    """
    
    print("\nAll interactions above have been logged via osmosis_wrap!")
    
except Exception as e:
    print(f"Error: {str(e)}")
    import traceback
    traceback.print_exc() 