import cmath
def quadratic(a,b,c):
  d = (b**2) - (4*a*c)
  d_sq = cmath.sqrt(d)
  pos_first_half = -b + d_sq
  pos_res = pos_first_half / (2*a)
  neg_first_half = -b - d_sq
  neg_res = neg_first_half / (2*a)
  return pos_res, neg_res
# Trial
print(quadratic(1,2,3))
