import os
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def check_environment():
    logger.info("Starting environment check...")
    
    # Check Python version
    logger.info(f"Python version: {sys.version}")
    
    # Check Android SDK
    sdk_path = os.environ.get('ANDROIDSDK')
    logger.info(f'Android SDK path: {sdk_path}')
    if (sdk_path and os.path.exists(sdk_path)):
        logger.info('✓ Android SDK path exists')
        # Check specific SDK components
        components = ['platform-tools', 'build-tools', 'platforms']
        for component in components:
            path = os.path.join(sdk_path, component)
            if os.path.exists(path):
                logger.info(f'✓ Found {component} at {path}')
            else:
                logger.error(f'✗ Missing {component} at {path}')
    else:
        logger.error('✗ Android SDK path does not exist')

    # Check Android NDK
    ndk_path = os.environ.get('ANDROIDNDK')
    logger.info(f'Android NDK path: {ndk_path}')
    if ndk_path and os.path.exists(ndk_path):
        logger.info('✓ Android NDK path exists')
    else:
        logger.error('✗ Android NDK path does not exist')
        logger.info('Please install Android NDK through Android Studio')

    # Check PATH
    path = os.environ.get('PATH')
    logger.info('Checking PATH environment variable...')
    paths = path.split(os.pathsep)
    sdk_in_path = any('Android\Sdk' in p for p in paths)
    logger.info(f'Android SDK in PATH: {"✓" if sdk_in_path else "✗"}')

if __name__ == '__main__':
    check_environment()
