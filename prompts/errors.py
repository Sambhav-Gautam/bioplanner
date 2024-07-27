error_messages = {
    "IndentationError": "IndentationError: There are indentation errors in one or \
        more of your function definitions. Functions should have at least one indented \
        line that has code and not comments in it. This can simply be a return or pass \
        statement.",
    "SyntaxError": "SyntaxError: There are syntax errors in one or more of your function \
        definitions or in your main code.",
    "NoParametersWarning": "NoParametersWarning: One or more of your functions does not \
        have any parameters. Functions typically have parameters to better describe the \
        experiment.",
    "CommentError": "CommentError: Your function includes a comment or docstring. Functions \
        should be named to sufficiently describe their purpose without the need for comments. \
        Please remove the comment or docstring and try again. Consider renaming your function \
        to better describe its purpose.",
    "MissingUnitsWarning": "MissingUnitsWarning: One or more of your function parameter \
        calls include numbers but do not include the units for said numbers. You may be missing \
        units that are important for describing the experiment.",
    "NoFunctionsError": "NoFunctionsError: There do not appear to be any functions in your \
        code. Please define functions",
    "NewFunctionError": "NewFunctionError: You have defined a new function. Please only use \
        the pseudofunctions provided.",
    "NoMainCodeError": "NoMainCodeError: You have not written any pseudocode in the main \
        code section.",
    "UndefinedFunctionError": "UndefinedFunctionError: You have used a function that is not \
        defined in the pseudofunctions provided.",
    "MissingUnitsWarning": "MissingUnitsWarning: One or more of your function parameter \
        calls include numbers but do not include the units for said numbers. You may be \
        missing units that are important for describing the experiment."
}