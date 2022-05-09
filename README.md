<h1 align="center">vk_captchasolver - VKontakte captcha solver with 91% accuracy right.</h1>

<h2>This model, which solves vkontakte captchas, was taken from <a href="https://github.com/Defasium/vkCaptchaBreaker/">Defasium's repository</a></h2>

<h1 align="center"> -How to use?- </h1>

<h2 align="center"> -Solve by image- </h2>

```python
import vk_captchasolver as vc

captcha = vc.solve(image='captcha.png')
print(captcha)
```

<h2 align="center"> -Solve by sid and s- </h2>

```python
import vk_captchasolver as vc

captcha = vc.solve(sid=74838345480543, s=1) #Solve by sid and s
captcha = vc.solve(sid=74838345480543) #Solve by sid only
print(captcha)
```