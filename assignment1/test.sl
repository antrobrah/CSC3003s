/*
float bisect ()
//  solve x*x = 2 using bisection 
//  find zero of f(x) = x*x-2 
{
  float l,r,m,fm,afm,eps;

  l = 0;			// left end of interval
  eps = 0.0001;
  r = 10;			// right end of interval
  m = (l+r)/2;			// midpoint of interval
  fm = m*m-2;			// f(m)}
  if (fm<0) afm = -fm;
      else afm = fm;	// abs(f(m))
  while (afm>eps)
  {
    if (fm>0) r = m; else l = m;
    m = (l+r)/2;
    fm = m*m-2;
    if (fm<0) afm = -fm; else afm = fm;
  }
  return m;
}
*/
1st_value
1.
3.9f
0.9e-10F
1.f
0.E1f
int main() {
    int a = 8;
    int c = 6;
    if(c<=a)
      // do something here
    else
      // do something else here
}
