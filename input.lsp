(import "os")

(invoke os.path "basename" "foo/bar")

(define eleven (let ((x (int 7)) (y (int 9)))  (int 11)))

(define I (lambda (x) x))

(import "sys")

(define stderr sys.stderr)

(invoke stderr "write" "crap\n")

(for x  (int 7)  (not x))

(try (int 7) (catch eid  eid))