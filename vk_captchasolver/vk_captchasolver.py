# -*- coding: utf-8 -*-
from PIL import Image
from requests import get
from os.path import dirname, abspath, join
from os import remove
from random import randint as rnt
import numpy as np
import onnxruntime as rt

CDIR = dirname(abspath(__file__))

def solve(image=None, sid=None, s=None):
	if sid == None or s == None:
		img = Image.open(image).resize((128, 64)).convert('RGB')
	else:
		fname = 'cap{}tcha.png'.format(rnt(-99999999999, 99999999999))
		with open(join(CDIR, fname), 'wb') as f:
			f.write(get('https://api.vk.com/captcha.php?sid={}&s={}'.format(sid, s)).content)
		img = Image.open(join(CDIR, fname)).resize((128, 64)).convert('RGB')

	x = np.array(img).reshape(1, -1)
	x = np.expand_dims(x, axis=0)
	x = x/np.float32(255.)

	session = rt.InferenceSession(join(CDIR, 'captcha_model.onnx'))
	session2 = rt.InferenceSession(join(CDIR, 'ctc_model.onnx'))

	out = session.run(None, dict([(inp.name, x[n]) for n, inp in enumerate(session.get_inputs())]))
	out = session2.run(None, dict([(inp.name, np.float32(out[n])) for n, inp in enumerate(session2.get_inputs())]))

	codemap = ' 24578acdehkmnpqsuvxyz'

	captcha = ''.join([codemap[c] for c in np.uint8(out[-1][out[0]>0])])
	if image == None:
		remove(join(CDIR, fname))
	return captcha