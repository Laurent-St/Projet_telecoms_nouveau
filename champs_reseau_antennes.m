%réseau d'antenne et champs lointain
function E_module = champs_reseau_antennes()

f = 2.45 * 10^(9);
w = 2* pi * f;
mu_0 = 4 * pi * 10^(-7);
c = 3 * 10^(8);
beta=w/c;
lambda = 2* pi / beta;
l = lambda * 0.5;%hauteur du dipole ici antenne lambda demi
I_0 = 5.32 * 10^(-2);%valeur du courant... le meme que celui dans le projet du coup 
r = 100;%distance en mètre séparant le centre du réseau et le récepteur
d = lambda / sqrt(2);%distance entre les deux antennes (libre) --> d=0.0866
disp(d);
theta = pi/4;%angle entre milieu du réseu et récepteur par rapport à la verticale


E_module = ( w * mu_0 * l * I_0 * sin(theta))/(4 * pi * r) * cos(beta * d * cos(theta) * 0.5)
