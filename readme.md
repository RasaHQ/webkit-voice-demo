# webkit speech rasa demo 

In this demo project we're building a small frontend service that
can communicate with Rasa. The goal of this project is two-fold. 

1. We'll have a demo that shows how you might be able to build 
your own front-end javascript tools on top of Rasa. 
2. We'll show how you can connect the browser's 
[speech detection](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis)
tools to Rasa. Note that these tools are experimental and that
browser support will vary. 

## How to Run 

To run this project locally you'll need to first install all 
the requirements and create a new Rasa project. You can do all
of this by running a provided make command. 

```bash
make init
```

> If you're only interested in installing the tools you can also 
> run `make install`. This allows you to copy your own Rasa project
> without starting a new one.

Once this is done you'll need to start two services locally. 

```bash
# The rasa backend that we'll communicate to. 
rasa run --verbose --enable-api
# The front end service that relays requests.
uvicorn app:app --reload --port 8000
```

Once both services are running you can go to `localhost:8000` to 
literally "talk" to Rasa. 

## Permissions 

If you're using Chrome then you may need to give explicit permissions
to allow the browser to record your audio. If you don't want to get 
blocked it helps to take two steps:

1. As per the guide [here]() 
you'll want to point your browser to `chrome://flags/#unsafely-treat-insecure-origin-as-secure` and flag 
`localhost:8000` as allowed. 
2. From here, you might either need to restart your OS/browser. Alternatively
you can also start a new browser using incognito mode.