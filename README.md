# The-Simple-Pendulum

Derivation of the pendulum formula
<h6>Now the Ligrangian is defined as</h6>
<img src="http://www.sciweavers.org/tex2img.php?eq=L%20%3D%20T%20-%20V&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="Ligrangian" width="79" height="17" />

###### where T(kinetic energy) and V(Potential Energy)

###### Now the kinetic energy is defined as 

<img src="http://www.sciweavers.org/tex2img.php?eq=T%20%3D%20%5Cfrac%7B1%7D%7B2%7Dmv%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="T = \frac{1}{2}mv^2" width="86" height="43" />. 

###### However we can split this up into a vertical and horizontal component as follows

<img src="http://www.sciweavers.org/tex2img.php?eq=T%20%3D%20%5Cfrac%7B1%7D%7B2%7Dm%28v_%7Bx%7D%5E2%2Bv_%7By%7D%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="T = \frac{1}{2}m(v_{x}^2+v_{y}^2)" width="143" height="43" />

###### Now from the diagram we can see using trignometry that
<img src="http://www.sciweavers.org/tex2img.php?eq=r%20%3D%20%5Cbegin%7Bcases%7Dr_%7Bx%7D%20%3D%20r%20sin%28%5Ctheta%28t%29%29%20%5C%5Cr_%7By%7D%20%3D%20r%20cos%28%5Ctheta%28t%29%29%5Cend%7Bcases%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="r = \begin{cases}r_{x} = r sin(\theta(t)) \\r_{y} = r cos(\theta(t))\end{cases}" width="165" height="47" />

###### From this we can get the derivative is
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cdot%7Br%7D%20%3D%20%5Cbegin%7Bcases%7D%5Cdot%7Br_%7Bx%7D%7D%20%3D%20r%5Cdot%7B%5Ctheta%28t%29%7D%20cos%28%5Ctheta%28t%29%29%20%5C%5C%5Cdot%7Br_%7By%7D%7D%20%3D%20-r%5Cdot%7B%5Ctheta%28t%29%7D%20sin%28%5Ctheta%28t%29%29%5Cend%7Bcases%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\dot{r} = \begin{cases}\dot{r_{x}} = r\dot{\theta(t)} cos(\theta(t)) \\\dot{r_{y}} = -r\dot{\theta(t)} sin(\theta(t))\end{cases}" width="207" height="49" />

###### Finally the kinetic energy is then
<img src="http://www.sciweavers.org/tex2img.php?eq=T%20%3D%20%5Cfrac%7B1%7D%7B2%7Dm%28%5Cdot%7B%5Ctheta%28t%29%7D%5E2r%5E2cos%5E2%28%5Ctheta%29%2B%5Cdot%7B%5Ctheta%7D%5E2r%5E2%20sin%5E2%28%5Ctheta%28t%29%29%29%20%3D%20%5Cfrac%7B1%7D%7B2%7Dmr%5E2%5Cdot%7B%5Ctheta%7D%5E2&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="T = \frac{1}{2}m(\dot{\theta(t)}^2r^2cos^2(\theta)+\dot{\theta}^2r^2 sin^2(\theta(t))) = \frac{1}{2}mr^2\dot{\theta}^2" width="429" height="43" />

###### Now similarly we the potential energy we have
<img src="http://www.sciweavers.org/tex2img.php?eq=V%20%3D%20mgh%20%3D%20-mgrcos%28%5Ctheta%28t%29%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="V = mgh = -mgrcos(\theta(t))" width="222" height="19" />
<h6>Now we have made the point of 0 potential energy at y=0 therefore all heights below it will be negitive
so now the ligrangian becomes</h6>

<img src="http://www.sciweavers.org/tex2img.php?eq=L%20%3D%20%5Cfrac%7B1%7D%7B2%7Dmr%5E2%5Cdot%7B%5Ctheta%7D%5E2%20%2B%20mgrcos%28%5Ctheta%28t%29%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="L = \frac{1}{2}mr^2\dot{\theta}^2 + mgrcos(\theta(t))" width="233" height="43" />
###### Now the Euler legrange equation is
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7Bd%7D%7Bdt%7D%5Cfrac%7BdL%7D%7Bd%5Cdot%7B%5Ctheta%7D%7D-%5Cfrac%7BdL%7D%7Bd%5Ctheta%7D%20%3D%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\frac{d}{dt}\frac{dL}{d\dot{\theta}}-\frac{dL}{d\theta} = 0" width="125" height="44" />

###### And now solving for each component
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7BdL%7D%7Bd%5Cdot%7B%5Ctheta%7D%7D%20%3D%20mr%5E2%5Cdot%7B%5Ctheta%7D%20%5Crightarrow%20%5Cfrac%7Bd%7D%7Bdt%7D%5Cfrac%7BdL%7D%7Bd%5Cdot%7B%5Ctheta%7D%7D%20%3D%20mr%5E2%5Cddot%7B%5Ctheta%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\frac{dL}{d\dot{\theta}} = mr^2\dot{\theta} \rightarrow \frac{d}{dt}\frac{dL}{d\dot{\theta}} = mr^2\ddot{\theta}" width="232" height="44" />

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7BdL%7D%7Bd%5Ctheta%7D%20%3D%20-mgr%20sin%28%5Ctheta%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\frac{dL}{d\theta} = -mgr sin(\theta)" width="147" height="43" />

###### Therefore
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cddot%7B%5Ctheta%7D%20%2B%20%5Cfrac%7Bg%7D%7Br%7Dsin%28%5Ctheta%29%20%3D%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\ddot{\theta} + \frac{g}{r}sin(\theta) = 0" width="131" height="40" />
<h6>This is a differential equation which can now be solved for the angle theta from the vertical at any time t>0. However since this is a nonlinear second order nonautonomous homogenious differential equation it is best that it be solved numerically using a range kutta method. We can however obtain an analytical solution with ease by using the small angle formula. By expanding sin into a taylor series and taking the first order we get</h6>
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cddot%7B%5Ctheta%7D%20%2B%20%5Cfrac%7Bg%7D%7Br%7D%5Ctheta%20%3D%200&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\ddot{\theta} + \frac{g}{r}\theta = 0" width="92" height="40" />
###### and it can be shown with ease that the solution is

<img src="http://www.sciweavers.org/tex2img.php?eq=%5Ctheta%20%3D%20Ae%5E%7B%5Comega%20%5Cimath%7D%20%2B%20Be%5E%7B-%5Comega%20%5Cimath%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\theta = Ae^{\omega \imath} + Be^{-\omega \imath}" width="140" height="18" />

###### Now we can put it into a convienient form for initial conditions as follows
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Ctheta%20%3D%20A_%7B0%7Dcos%28%5Comega%20t%20%2B%20%20%5Cphi%29%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\theta = A_{0}cos(\omega t +  \phi) " width="153" height="19" /> where <img src="http://www.sciweavers.org/tex2img.php?eq=%5Comega%20%3D%20%5Csqrt%7B%5Cfrac%7Bg%7D%7Br%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\omega = \sqrt{\frac{g}{r}}" width="69" height="47" />
###### In this form A0 is the initial amplitude and phi is the initial angle



