import sys
import os
import logging
import logging.config
import yaml

path_to_add = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path_to_add)

log_dir = os.path.join(path_to_add, 'logs')
if os.path.isdir(log_dir) is False:
    print('Creating directory because {} doesnt exist'.format(log_dir))
    try:
        print('Creating directory...')
        os.mkdir(log_dir)
    except Exception as e:
        print("Exception creating directory: {}".format(e))

logging_path = os.path.join(path_to_add, 'loggingConfig.yml')
logs_path = os.path.join(path_to_add, 'logs', 'info.log')
with open(logging_path, 'rt') as f:
    config = yaml.safe_load(f.read())
    config['handlers']['file_handler']['filename'] = logs_path
    logging.config.dictConfig(config)
