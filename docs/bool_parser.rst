
.. contents:: Table of Contents
   :depth: 5


OPS
---


L0
==
- :not: !p
- :exist: ?
- :all:   \*

L1
==
- :and: p&q
- :or:  p|q

L2
==
- :if-p-then-notq-else-q: p^q      可交换  (p&!q)|(!p&q)       (p~>q)|(q~>p) 
- :if-p-then-notq-else-tru: p'q    可交换 !(p&q)      (!p|!q)
- :if-p-then-fls-else-notq: p"q    可交换 !(p|q)      (!p&!q)

L3
==
- :if-p-then-q-else-tru: p->q            !p|q
- :if-q-then-p-else-tru: p<-q            p|!q
- :if-p-then-notq-else-fls: p~>q         p&!q
- :if-q-then-notp-else-fls: p<~q         !p&q


L4
==
- :if-p-then-q-else-notq: p<->q   可交换  (p&q)|(!p&!q)    (!p|q)&(p|!q)


OTHERS
======
- :if-p-then-q-else-fls: p&q
- :if-q-then-p-else-fls: p&q
- :if-p-then-tru-else-q: p|q
- :if-q-then-tru-else-p: p|q
- :if-notp-then-notq-else-tru: p|!q  !q|p  p<-q
- :if-notq-then-notp-else-tru: q|!p  !p|q  p->q
- :if-p-then-tru-else-fls: p
- :if-q-then-tru-else-fls: q
- :if-p-then-q-else-q: q
- :if-q-then-p-else-p: p
- :if-p-then-notq-else-notq: !q
- :if-q-then-notp-else-notp: !p
- :if-p-then-fls-else-tru: !p
- :if-q-then-fls-else-tru: !q
- :if-p-then-fls-else-q: !p&q q&!p p<~q
- :if-q-then-fls-else-p: p&!q  p~>q


ASSERTS
-------

- :if-p-then-q-else-tru-always-tru: p=>q
- :if-q-then-p-else-tru-always-tru: p<=q
- :if-p-then-q-else-notq-always-tru: p<=>q 可交换
