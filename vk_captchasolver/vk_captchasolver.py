# -*- coding: utf-8 -*-
from PIL import Image
from requests import get
from os.path import dirname, abspath, join as pjoin
from os import remove
from random import randint as rnt
from numpy import array, expand_dims, float32, uint8
from onnxruntime import InferenceSession

CDIR = dirname(abspath(__file__))

def solve(image=None, sid=None, s=None):
	if sid == None:
		img = Image.open(image).resize((128, 64)).convert('RGB')
	else:
		fname = 'cap{}tcha.png'.format(rnt(-99999999999, 99999999999))
		with open(pjoin(CDIR, fname), 'wb') as f:
			if s != None:
				f.write(get('https://api.vk.com/captcha.php?sid={}&s={}'.format(sid, s)).content)
			else:
				f.write(get('https://api.vk.com/captcha.php?sid={}'.format(sid)).content)
		img = Image.open(pjoin(CDIR, fname)).resize((128, 64)).convert('RGB')

	x = array(img).reshape(1, -1)
	x = expand_dims(x, axis=0)
	x = x/float32(255.)

	session = InferenceSession(pjoin(CDIR, 'captcha_model.onnx'))
	session2 = InferenceSession(pjoin(CDIR, 'ctc_model.onnx'))

	out = session.run(None, dict([(inp.name, x[n]) for n, inp in enumerate(session.get_inputs())]))
	out = session2.run(None, dict([(inp.name, float32(out[n])) for n, inp in enumerate(session2.get_inputs())]))

	codemap = ' 24578acdehkmnpqsuvxyz'

	captcha = ''.join([codemap[c] for c in uint8(out[-1][out[0]>0])])
	if image == None:
		remove(pjoin(CDIR, fname))
	return captcha