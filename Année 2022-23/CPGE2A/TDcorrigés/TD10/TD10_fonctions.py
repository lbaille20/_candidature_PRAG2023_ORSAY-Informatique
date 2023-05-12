# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.text.html
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle 

nrows, ncols = 6, 7
couleurs = {1: "orange", 2: "red"}

def image_jeu_init(numerotation = False):
    c, r = 1, 0.35
    dpi, f = 72, 0.8
    couleur_fond, couleur_vide = "blue", "white"
     
    c, r = f * c, f * r
    cell_width, cell_height = c, c
    rectangle_width, rectangle_height = ncols * c, nrows * c
    
    fig, ax = plt.subplots(figsize=(rectangle_width, rectangle_height), dpi=dpi)
    #fig.subplots_adjust(margin/width, margin/height,
    #                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(-c * numerotation - c/dpi, cell_width  * ncols + c/dpi)
    ax.set_ylim(-c * numerotation - c/dpi, cell_height * nrows + c/dpi)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()
    #https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.margins.html
    ax.margins(x=0, y= 0, tight=True)

    ax.add_patch(
        Rectangle(xy=(0, 0), width=ncols * c, height=nrows * c, #linewidth = 10,
                  facecolor=couleur_fond, edgecolor=couleur_fond)
    )
    if numerotation:
        for i in range(nrows):
            ax.add_patch(
                Rectangle(xy=(-c, c * i), width= c, height= c, #linewidth = 10,
                          facecolor=couleur_vide, edgecolor=couleur_fond)
            )
            ax.text(-c + c / 2, c * i + c / 2, str(nrows - 1 - i), fontsize = f * 20, fontweight="bold", 
                    horizontalalignment='center', verticalalignment='center')
    
        for j in range(ncols):
            ax.add_patch(
                Rectangle(xy=(0 + c * j, -c), width= c, height= c,
                          facecolor=couleur_vide, edgecolor=couleur_fond)
            )
            ax.text(0 + c * j + c / 2, -c + c / 2, str(j), fontsize = f * 20, fontweight="bold", 
                    horizontalalignment='center', verticalalignment='center')
    
    circles = [[None] * ncols for _ in range(nrows)]
    for i in range(nrows):
        for j in range(ncols):
            jeton = ax.add_patch(
                Circle(xy=(c * (j + 1 / 2), c * (i + 1 / 2)), radius = r,
                       facecolor=couleur_vide, edgecolor=couleur_vide)
            )
            circles[nrows - 1 - i][j] = jeton

    return fig, ax, circles

def image(jeu, nomfichier = None, numerotation=False):
    fig, ax, circles = image_jeu_init(numerotation)
    for i in range(nrows):
        for j in range(ncols):
            joueur = jeu['plateau'][i][j]
            if joueur != 0:
                circles[i][j].set(facecolor=couleurs[joueur], edgecolor=couleurs[joueur])
    if nomfichier == None:
        nomfichier = "image"
    #https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image
    plt.savefig(nomfichier + ".png",bbox_inches='tight')
    plt.show()
