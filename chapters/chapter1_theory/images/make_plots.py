import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.rc('font', family='sans-serif') 
matplotlib.rc('font', serif='Helvetica') 

def higgs_potential2d():
    mu2 = -1
    lam = 2

    r = np.arange(-1,1,.02)

    mu_pos = np.add(mu2*np.power(r,2), lam*np.power(r,4))

    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    ax.plot(r,mu_pos,'k',color="firebrick",linewidth=2)
    ax.set_ylim([-0.2,1])
    ax.grid(False)
    ax.set_title('')

    ax.set_aspect('equal')
    sns.despine(ax=ax, offset=0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    ax.yaxis.set_label_coords(.5, 1.03)
    plt.ylabel("$V(\phi)$", rotation="horizontal",ha='center', fontsize=16)

    plt.xlabel("$\phi$",ha='right', fontsize=16)
    ax.xaxis.set_label_coords(1, 0.125)

    # Vertical lines at vev
    vev = r[np.argmin(mu_pos)]
    plt.axvline(x=vev, linestyle="--", alpha=0.6)
    plt.axvline(x=-vev, linestyle="--", alpha=0.6)

    plt.annotate("$+v$", xy=(-vev,-.2), fontsize=12)
    plt.annotate("$-v$", xy=(vev,-.2), fontsize=12, ha="left")

    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.tight_layout()
    plt.savefig("higgs-2d-vev",bbox_inches='tight')


if __name__ == "__main__":
    higgs_potential2d()
    