from StringBuffer import StringBuffer

class Code(object):

    def __init__(self, spine, filename, lineno):
        self.spine = spine
        self.filename = filename
        self.lineno = lineno
        self.string = self.toString()


    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}:{1}@{2}'.format(self.string, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.string


    def toString(self):
        sb = StringBuffer()
        first = True
        sb.append('(')
        for c in self.spine:
            if first:
                first = False
            else:
                sb.append(' ')
            sb.append(str(c))
        sb.append(')')
        return str(sb)
    


class Leaf(object):

    def __init__(self, uni, filename, lineno):
        self.string = intern(str(uni))
        self.filename = filename
        self.lineno = lineno

    # repr's goal is to be unambiguous
    def __repr__(self):
        return '{0}:{1}@{2}'.format(self.string, self.filename, self.lineno)

    # str's goal is to be readable
    def __str__(self):
        return self.string

