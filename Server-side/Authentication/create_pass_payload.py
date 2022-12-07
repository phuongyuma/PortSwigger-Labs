a = open("D:\CMC\Web Application Security\Portswigger\Authentication\candidate_pass.txt", "r")
b = open("D:\CMC\Web Application Security\Portswigger\Authentication\payload_pass.txt", "w")
length = 0
for i in a:
    b.write(i)
    b.write("peter\n")
    length = length + 1

