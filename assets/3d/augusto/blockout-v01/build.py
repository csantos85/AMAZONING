"""Blender 4.3.2: proposed head volumes, not an approved identity asset.
Run from repo root: blender -b -t 2 --python assets/3d/augusto/blockout-v01/build.py
"""
import bpy
import math
import json
import hashlib
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
REF = ROOT / 'assets/concept-art/pai-de-jeff/pai_jeff_scratch_art_v01_candidata.png'
assert hashlib.sha256(REF.read_bytes()).hexdigest() == '9d671db4633a856495839debaec84685f2c70dc45c2e6201870924a6dea2cde8'
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def mat(name, color):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    return m

clay = mat('Clay - proposed volumes', (.46, .43, .39))
hair = mat('Hair mass - provisional', (.12, .12, .13))
gray = mat('Temple gray - provisional', (.32, .33, .34))
eye = mat('Eye placeholder - no canonical color', (.65, .65, .63))
dark = mat('Facial guides', (.18, .17, .16))

def mesh(name, verts, faces, material):
    data = bpy.data.meshes.new(name)
    data.from_pydata(verts, [], faces)
    data.update()
    ob = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(ob)
    ob.data.materials.append(material)
    ob['status'] = 'PROPOSTA - NAO APROVADA'
    return ob

def ellipsoid(name, location, scale, material, segments=32):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=16, location=location)
    ob = bpy.context.object
    ob.name = name
    ob.scale = scale
    ob.data.materials.append(material)
    for p in ob.data.polygons:
        p.use_smooth = True
    ob['status'] = 'PROPOSTA - NAO APROVADA'
    return ob

def line(name, points, radius, material):
    curve = bpy.data.curves.new(name, 'CURVE')
    curve.dimensions = '3D'
    curve.bevel_depth = radius
    curve.bevel_resolution = 2
    sp = curve.splines.new('POLY')
    sp.points.add(len(points)-1)
    for p, co in zip(sp.points, points):
        p.co = (*co, 1)
    ob = bpy.data.objects.new(name, curve)
    bpy.context.collection.objects.link(ob)
    curve.materials.append(material)
    return ob

# Front faces -Y; all units are arbitrary study units, not body measurements.
rings = [
    (.00, .24, .48, .36), (.14, .44, .58, .45),
    (.38, .60, .55, .52), (.65, .65, .56, .58),
    (.93, .66, .60, .63), (1.20, .64, .58, .66),
    (1.48, .61, .53, .67), (1.72, .56, .46, .60),
    (1.89, .41, .32, .43), (1.98, .10, .09, .12),
]
verts=[]
n=32
for z, width, front, back in rings:
    for i in range(n):
        a=2*math.pi*i/n
        c=math.cos(a)
        # Slightly square transverse sections for jaw planes.
        x=width*math.copysign(abs(math.sin(a))**.82, math.sin(a))
        y=-(front if c>=0 else back)*math.copysign(abs(c)**.72,c)
        verts.append((x,y,z))
faces=[]
for j in range(len(rings)-1):
    for i in range(n):
        a=j*n+i; b=j*n+(i+1)%n
        faces.append((a,b,b+n,a+n))
faces += [tuple(reversed(range(n))), tuple((len(rings)-1)*n+i for i in range(n))]
head=mesh('HEAD - angular cranium and jaw proposal',verts,faces,clay)
bevel=head.modifiers.new('Small plane transitions','BEVEL')
bevel.width=.025; bevel.segments=2
ellipsoid('NECK - provisional', (0,.14,-.28),(.34,.36,.52),clay)
ellipsoid('BASE - not body proportions', (0,.16,-.65),(.75,.43,.13),clay)

# Explicit sculpting placeholders, intentionally separate/editable.
mesh('NOSE - bridge and tip proposal',
     [(-.10,-.57,1.20),(.10,-.57,1.20),(-.12,-.85,.73),(.12,-.85,.73),
      (-.17,-.61,.66),(.17,-.61,.66),(0,-.90,.73)],
     [(0,1,3,6,2),(0,2,4),(1,5,3),(2,6,3,5,4),(0,4,5,1)],clay)
for sign in [-1,1]:
    ellipsoid('EAR '+str(sign), (sign*.665,.025,.86),(.105,.18,.25),clay)
    ellipsoid('EYE narrow placeholder '+str(sign),(sign*.29,-.57,1.015),(.19,.055,.065),eye)
    ellipsoid('IRIS neutral guide '+str(sign),(sign*.29,-.625,1.015),(.037,.012,.038),dark)
    # Brows slope down toward bridge; no inferred exact measurements.
    line('BROW '+str(sign),[(sign*.12,-.62,1.10),(sign*.28,-.64,1.17),(sign*.48,-.55,1.20)],.038,hair)
    line('LOWER EYE GUIDE '+str(sign),[(sign*.12,-.60,.97),(sign*.29,-.61,.955),(sign*.46,-.55,.98)],.012,clay)
    ellipsoid('TEMPLE gray mass '+str(sign),(sign*.59,.05,1.38),(.055,.32,.30),gray)
line('MOUTH guide',[(-.23,-.565,.405),(0,-.61,.42),(.23,-.565,.405)],.014,dark)
line('LOWER LIP plane',[(-.13,-.585,.365),(0,-.605,.35),(.13,-.585,.365)],.018,clay)

# Hair silhouette block: swept-back wedges, not final strand design.
ellipsoid('HAIR cap proposal',(0,.10,1.73),(.61,.61,.38),hair)
for i in range(-3,4):
    x=i*.15
    mesh('HAIR swept wedge '+str(i),
         [(x-.12,-.46,1.64),(x+.12,-.46,1.64),(x+.13,.32,1.96),
          (x-.10,.32,1.96),(x+.07,.53,2.12-abs(i)*.035)],
         [(0,1,2,3),(0,3,4),(3,2,4),(2,1,4),(1,0,4)],hair)

ref_image=bpy.data.images.load(str(REF),check_existing=True)
ref_image.pack()
bpy.ops.object.empty_add(type='IMAGE', location=(2.1,.8,1.0))
reference=bpy.context.object
reference.name='APPROVED PORTRAIT - compare, do not modify'
reference.data=ref_image
reference.empty_display_size=2.8
reference.rotation_euler=(math.pi/2,0,0)
reference.hide_render=True

scene=bpy.context.scene
scene.render.engine='BLENDER_WORKBENCH'
scene.render.resolution_x=720
scene.render.resolution_y=900
scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.display.shading.light='STUDIO'
scene.display.shading.color_type='MATERIAL'
scene.display.shading.show_shadows=True
scene.display.shading.show_cavity=True
scene.display.shading.cavity_type='BOTH'
scene.display.shading.background_type='WORLD'
scene.world.color=(.065,.065,.065)
scene.view_settings.view_transform='Standard'
scene['STATUS']='PROPOSTA - blockout nao aprovado; sem rig; nao fiel integralmente'
scene['REFERENCE_SHA256']=hashlib.sha256(REF.read_bytes()).hexdigest()
scene['UNITS']='Arbitrary study units; not canonical dimensions'
cameras=[]
for name,pos in [('frente',(0,-8,.78)),('perfil',(8,0,.78)),('tres-quartos',(5,-8,1.05))]:
    bpy.ops.object.camera_add(location=pos)
    cam=bpy.context.object
    cam.name='CAM '+name
    cam.rotation_euler=(Vector((0,0,.78))-cam.location).to_track_quat('-Z','Y').to_euler()
    cam.data.type='ORTHO'; cam.data.ortho_scale=3.45
    cameras.append(cam)
scene.camera=cameras[2]
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'augusto_cabeca_blockout_v01.blend'))
for cam in cameras:
    scene.camera=cam
    scene.render.filepath=str(OUT/(cam.name[4:]+'.png'))
    bpy.ops.render.render(write_still=True)
manifest={'blender':bpy.app.version_string,'status':'PROPOSTA - NAO APROVADA','reference_sha256':scene['REFERENCE_SHA256'],
          'files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.suffix in ['.blend','.png']}}
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
