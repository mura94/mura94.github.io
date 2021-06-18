#Define color pallete
redBar = '#ECCFC2'
oneWeekDecreaseColor = '#ABEDC0'
borderColor = '#D9B596'
increaseColor = '#F20505'
decreaseColor = '#007509'
titleColor = '#364959'
labelColor = '#706D65'

#Color scale pallette
light = '#FAF2ED'
medLight = '#FBE1C3'
medium = '#FAC697'#FDE3C3'
medDark = '#D98E73'#F5D6C6'
medDark2 = '#D9765F'
dark = '#702B15'


#Sets each spine to a more subtle color and width
def formatBorder(ax):
    for spineName in ax.spines:
        ax.spines[spineName].set_color(borderColor)
        ax.spines[spineName].set_linewidth(2)
        
#Returns a tuple that pairs two contrasting colors for the face and data display respectively
def getContrastingColors(weeksClimbing):
    if(weeksClimbing >= 5):
        return (medDark2, light)
    if(weeksClimbing >= 4):
        return (medDark, light)
    if(weeksClimbing >= 3):
        return (medium, dark)
    if(weeksClimbing >= 2):
        return (medLight, dark)
    return (light, dark)

# Returns the difference between the most recent increase and the prevous day's
def getLastIncreaseChange(state, df):
    return int(df[state][0]) - int(df[state][1])

# Returns a positive sign string if increase >= 0 (for annotation strings)
def getIncreaseSign(increase):
    if(increase >= 0):
        return '+'
    else:
        return ''

#Returns a color based on the sign of the relative increase (green=less, red=more)
def getIncreaseColor(increase):
    if(increase >= 0):
        return increaseColor
    else:
        return decreaseColor

#Annotations to help read the charts
guideArrow = dict(arrowstyle='wedge',
                        connectionstyle="angle3", color=medDark, relpos = (1, 0.5))

guideMark = dict(arrowstyle='-',
                        color=increaseColor, relpos = (0.5, 0))

def createLabelGuide(ax, text, xy, xycoords, textypos):
    ax.annotate(s=text,xy=xy, xytext=(-.3, textypos), 
                            textcoords='axes fraction', xycoords=xycoords, fontsize=11,
                            color=labelColor, horizontalAlignment='right',
                            arrowprops=guideArrow)