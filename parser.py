from lark import Lark

grammar = """
    start: program

    program: expr*

    expr: number+ semi_colon?
        | STRING -> str
        | arithmetic_expr -> arith_expr

    arithmetic_expr: number bin_op number

    bin_op: "+" -> plus | "-" -> minus | "*" -> mult | "/" -> div | "%" -> mod

    number: INTEGER -> int
          | FLOAT -> float

    // define tokens
    INTEGER: /\d+/
    FLOAT: /\d+\.\d+/
    STRING: /"\w*"/
    semi_colon: ";"
    left_paren: "("
    right_paren: ")"
    left_curly: "{"
    right_curly: "}"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='start',parser='lalr')

def parse_input(input_string):
    tree = parser.parse(input_string)
    print(tree.pretty())

if __name__ == "__main__":
    input_string = None
    with open('./input.txt','r') as file:
        input_string = file.read()
    parse_input(input_string)
