
from ..eval.Code import SExpression, Atom, StringLiteral, Syntax

from .Continuation import TopCont

EVAL     = 0
CONTINUE = 1
RETURN   = 2
DONE     = 3


class State(object):

    def __init__(self, interpreter, exp, env):
        self.interpreter = interpreter
        self.tag = EVAL
        self.val = None
        self.exp = exp
        self.env = env
        self.k = TopCont()


    def isDone(self):
        return self.tag is DONE


    def step(self):

        if self.tag is EVAL:

            if  self.exp is None:
                self.val = None
            elif isinstance(self.exp, StringLiteral):
                self.val = exp.string
            elif isinstance(self.exp, Atom):
                self.val = self.lookup(exp, env)
            elif isinstance(self.exp, SExpression):


                code = self.exp.code

                if code is Syntax.SEQ:
                    pass
                elif code is Syntax.LET:
                    pass
                elif code is Syntax.DEFINE:
                    pass
                elif code is Syntax.LAMBDA:
                    pass
                elif code is Syntax.INVOKE:                    
                    pass
                elif code is Syntax.APPLY:
                    pass
                elif code is Syntax.PRIMITIVE_DATA_OP:
                    pass
                elif code is Syntax.UNARY_OP:
                    pass
                elif code is Syntax.BINARY_OP:                    
                    pass
                elif code is Syntax.TERNARY_OP:
                    pass
                elif code is Syntax.AMBI1_OP:
                    pass
                elif code is Syntax.AMBI2_OP:
                    pass
                elif code is Syntax.N_ARY_OP:                    
                    pass
                elif code is Syntax.TRY:
                    pass
                elif code is Syntax.FOR:
                    pass
                elif code is Syntax.QUOTE:
                    pass
                elif code is Syntax.CATCH:
                    pass
                else:
                   raise PLambdaException("Unhandled form in State.step")
                #FIXME: we are done when this can be removed.
                self.val = self.interpreter.evalSExpression(self.exp, self.env)
            else:
                self.val = self.exp

            self.tag = RETURN

            
        elif self.tag is CONTINUE:
            self.k.cont(self)
        elif self.tag is RETURN:
            self.k.ret(self)
        elif self.tag is DONE:
            pass
        else:
            pass

        return
