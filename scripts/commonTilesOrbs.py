import compararTiles_listwithOrb as tiles_Orb
import collections
caat =  [x + '_' + y for x, values in tiles_Orb.dictArqRegCaat.items() for y in values]
mat = [x + '_' + y for x, values in tiles_Orb.dictArqRegMAtla.items() for y in values]
pan = [x + '_' + y for x, values in tiles_Orb.dictArqRegPan.items() for y in values]

orbitas = []
orbitas.extend(caat)
orbitas.extend(mat)
orbitas.extend(pan)

repetidas = [item for item, count in collections.Counter(orbitas).items() if count > 1]
# print(repetidas)

rep_orb = []
for r in repetidas:
    aux = ""
    if r in caat:
        aux = "_caat"
    if r in mat:
        aux = aux + "_MAtla"
    if r in pan:
        aux = aux + "_pan"
    rep_orb.append(r+aux)
print(rep_orb)