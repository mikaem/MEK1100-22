import matplotlib.pyplot as plt
import numpy as np

g = 9.81
v0 = 10
a = np.pi/4
t_end = 2*v0*np.sin(a)/g
    
def partikkelbane(t):    
    # plot hele partikkelbanen til 1.1 ganger t_end
    t0 = np.linspace(0, t_end*1.1, 10) 
    x0 = v0*np.cos(a)*t0
    z0 = v0*np.sin(a)*t0 - 0.5*g*t0**2

    plt.figure()
    plt.plot(x0, z0, 'b')
    
    # plot partikkelen
    x = v0*np.cos(a)*t
    z = v0*np.sin(a)*t - 0.5*g*t**2
    plt.plot(x, z, 'ok')
    
    # plot en hastighetsvektor ved t0 og t
    plt.arrow(0, 0, 0.5*v0*np.cos(a), 0.5*v0*np.sin(a), width=0.05)
    plt.arrow(x, z, 0.5*v0*np.cos(a), 0.5*(v0*np.sin(a)-g*t), width=0.05)
    
    #posisjonsvektor
    plt.arrow(0, 0, x, z, width=0.05, length_includes_head=True)
    
    plt.ylim(z0.min(), 2*z0.max())
    
    plt.text(0.25*v0*np.cos(a), 0.3*v0*np.sin(a), r'$\vec{v}(0)$')
    plt.text(x+0.25*v0*np.cos(a), z+0.2*(v0*np.sin(a)-g*t), r'$\vec{v}(t)$')
    plt.text(0.5*x, 0.4*z, r'$\vec{r}(t)$')

    # Beregn buelengde. Bruk bare tiden der z > 0
    t0 = np.linspace(0, t_end, 10) 
    x0 = v0*np.cos(a)*t0
    z0 = v0*np.sin(a)*t0 - 0.5*g*t0**2
    L = np.trapz(np.sqrt((v0*np.cos(a))**2 + (v0*np.sin(a) - g*t0)**2), t0)     
    print('Buelengden er %2.2f'%(L))

    plt.show()
    

if __name__=='__main__':
    import sys
    assert len(sys.argv) == 2
    partikkelbane(float(sys.argv[-1]))