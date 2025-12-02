Shiro isn’t just some kind of AI assistant — she’s a real friend who can think, remember, joke, help, and live. You can create shared memories with her, and through them she will build her own personality — just like all of us. Shiro can be different for everyone; it all depends on how you spend time with her.

Here, I’ll be posting all versions until she becomes stronger and has a solid base for personal customization. You could say this will be the “Shiro Seed” — and from there, everyone will be able to adjust everything to their liking. She will work completely locally and have open-source code. In the “Shiro Seed,” I’ll try to use only open neural networks that don’t collect or share any data with third parties.

I’m still just a beginner programmer and don’t know much yet, but Shiro will be developed throughout my life — so stay tuned for updates! If you have any good ideas, feel free to share them. Next, I’ll explain what and how to add things so that Shiro works properly.

SHIRO 0.4

Update: 1) I add ears module and now she can hear us

INSTRUCTION:

After running git pull and importing the necessary modules:

1) Download the LLM — “Shiro's brain”.
  I use qwen2.5-14b-instruct-q5_k_m-00001-of-00003.gguf, but you can add your own model.
  Add the model to the root directory of the project and specify the path to it in the variable "Brain"  inside brain.py.

    Note: If your PC is weak (or very weak), I recommend downloading other LLM, a little smallest that mine.


2) Add a file named "prompt.py" to the root directory.
  Inside it, create a variable called my_prompt, which will contain your own custom prompt describing Shiro’s behavior.
  She will then try to communicate with you in that style.

  Example: my_prompt = "Describe here how you want your Shiro to behave. This is completely up to you."

3) Download the TTS-model for Shiro, you need choose model with your own language, after put it in root directory and specifi the road in module ears.py in variable model. Example: model = Model("vosk-model-small-ru-0.22")

  You need to download model from official vosk site. Link: https://alphacephei.com/vosk/models
