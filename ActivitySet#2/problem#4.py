def get_cs():
  """get string input"""
  a=input("Enter the string: ")
  return a


def cs_to_lot(cs):
    ''''''convert connected string to list of strings'''
    final=[]
    x=cs.split(';')
    for i in x:
        y=i.split('=')
        z=tuple(y)
        final.append(z)
    return final

def lot_to_cs(lot):
    """convert list of strings to connected string"""
    final=''
    for i in lot:
        eql=i[0]+'='+i[1]
        col=eql+';'
        final+=col
    size=len(final)
    return final[:size-1]
#sone