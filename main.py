import asyncio
from pathlib import Path
from loguru import logger

from src.utils.config import load_config
from src.agents.search_agent import SearchAgent

async def main():
    # Load configuration
    config = load_config()
    
    # Setup logging
    logger.add(
        Path(config['logging']['file']),
        level=config['logging']['level'],
        format=config['logging']['format']
    )
    
    # Initialize search agent
    agent = SearchAgent(config)
    
    try:
        # Example search
        results = await agent.search('your search query here')
        logger.info(f'Found {len(results)} results')
        
        # Process results
        processed_results = await agent.process_results(results)
        logger.info(f'Processed {len(processed_results)} results')
        
    except Exception as e:
        logger.error(f'Error during search: {str(e)}')
        raise

if __name__ == '__main__':
    asyncio.run(main())
