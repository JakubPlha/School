import random

a = random_randrange = random.randint (-10000, 10000)
print(a)

b = random_randrange = random.randint (-10000, 10000)
print(b)

c = random_randrange = random.randint (-10000, 10000)
print(c)

d = random_randrange = random.randint (-10000, 10000)
print(d)

e = random_randrange = random.randint (-10000, 10000)
print(e)

f = random_randrange = random.randint (-10000, 10000)
print(f)

g = random_randrange = random.randint (-10000, 10000)
print(g)

h = random_randrange = random.randint (-10000, 10000)
print(h)

ch = random_randrange = random.randint (-10000, 10000)
print(ch)

i = random_randrange = random.randint (-10000, 10000)
print(i)

j = random_randrange = random.randint (-10000, 10000)
print(j)

k = random_randrange = random.randint (-10000, 10000)
print(k)

print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )
print( )

tmp = (a + b) + (c + d) + (e + f) + (g + h) + (ch + i) + (j + k)
print(tmp, ("  toto je tmp"))

if tmp > 5000:
    ba = random.uniform (0.1, 5)
    print(ba, ("  toto je ba"))
    tmp_a = tmp * ba
    print(tmp_a, ("  toto je tmp_a"))

    if tmp_a > 10000:
        bc = random.uniform (0.1, 5)
        print(bc, ("  toto je bc"))
        tmp_b = tmp_a * bc
        print(tmp_b, ("  toto je tmp_b"))

        if tmp_b > 20000:
            bd = random.uniform (0.1, 5)
            print(bd, ("  toto je bd"))
            tmp_c = tmp_b * bd
            print(tmp_c, ("  toto je tmp_c"))

            if tmp_c > 40000:
                be = random.uniform (0.1, 5)
                print(be, ("  toto je be"))
                tmp_d = tmp_c * be
                print(tmp_d, ("  toto je tmp_d"))

                if tmp_d > 80000:
                    bf = random.uniform (0.1, 5)
                    print(bf, ("  toto je bf"))
                    tmp_e = tmp_d * bf
                    print(tmp_e, ("  toto je tmp_e"))

if tmp < -5000:
    ab = random.uniform (0.1, 2.5)
    print(ab, ("  toto je ab"))
    tmp_h = tmp * ab
    print(tmp_h, ("  toto je tmp_h"))

    if tmp_h < -10000:
        ac = random.uniform (0.1, 2.5)
        print(ac, ("  toto je ac"))
        tmp_ch = tmp_h * ac
        print(tmp_ch, ("  toto je tmp_ch"))

        if tmp_ch < -20000:
            ad = random.uniform (0.1, 2.5)
            print(ad, ("  toto je ad"))
            tmp_i = tmp_ch * ad
            print(tmp_i, ("  toto je tmp_i"))

            if tmp_i < -40000:
                ae = random.uniform (0.1, 2.5)
                print(ae, ("  toto je ae"))
                tmp_j = tmp_i * ae
                print(tmp_j, ("  toto je tmp_j"))

                if tmp_j < -80000:
                    af = random.uniform (0.1, 2.5)
                    print(af, ("  toto je af"))
                    tmp_k = tmp_j * af
                    print(tmp_k, ("  toto je tmp_k"))

if tmp > -5000 and tmp < 5000:
    tmp_g = random_randrange = random.randint (-10000, 10000)
    print(tmp_g, ("  toto je tmp_g"))

    tmp_f = tmp * tmp_g 
    print(tmp_f, ("  toto je tmp_f"))