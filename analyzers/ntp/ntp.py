import copy
import json

from .. import AbstractParser
from . import SERVICE_SCHEMA

class Parser(AbstractParser):
  '''
  parse results of the `ntp` scanner.

  $ ntp --json "{result_file}.json" {address} 2>&1 | tee "{result_file}.log"
  '''

  def __init__(self):
    super().__init__()

    self.name = 'ntp'
    self.file_type = 'json'

  def parse_file(self, path):
    super().parse_file(path)

    with open(path) as f:
      result = json.load(f)

    identifier = f"{result['address']}:{result['port']}"
    if identifier in self.services:
      return

    service = copy.deepcopy(SERVICE_SCHEMA)
    service.update(result)
    self.services[identifier] = service
