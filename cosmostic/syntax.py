import json
from typing import List, Any

from cosmostic.enums import Syntax
from cosmostic.query import Parameter


class SyntaxClause:
    def __init__(self, syntax: Syntax, field: str, args: Any = None):
        self.syntax = syntax
        self.field = field
        self.args = args

    def __repr__(self):
        if self.args is None:
            return f"{self.syntax.value}({self.field})"
        elif isinstance(self.args, List):
            return f"{self.syntax.value}({self.field}, {json.dumps(self.args)})"
        elif isinstance(self.args, Parameter):
            return f"{self.syntax.value}({self.field}, @{self.args.name})"
        return f"{self.syntax.value}({self.field}, {self.args})"
