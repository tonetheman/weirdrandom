i made a gist

https://gist.github.com/tonetheman/8d4d20a80929c106733c7ef848f96b22

got the whole idea from here

https://blog.merovius.de/2018/01/15/generating_entropy_without_imports_in_go.html

In python we do not have channels so I tested the idea with servers and clients. Should work about the same way. Threads sending a 1 and 2 to a listening local server **should** be non-deterministic.

That is the idea at least.

tony