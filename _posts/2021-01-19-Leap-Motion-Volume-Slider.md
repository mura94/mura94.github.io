---
layout: post
title: Leap Motion Volume Slider
subtitle: Using a Leap Motion, Unity, and MRTK to control the system volume of my computer with my hands.
tags: [Unity, MRTK, Mixed Reality, AR, Utility]
---

# Leap Motion Volume Slider

So like many XR developers, I have more than a few unused devices collecting dust in my office. Each piece of neat tech had at one point held loads of potential for nifty gadgets and programs, only to be abandoned when the work required to bring those ideas to fruition gets to be a bit overwhelming, or when the next piece of tech comes along to restart the cycle.

One of these devices is a Leap Motion controller – a small USB camera dedicated to short-range hand and finger tracking. These have been a round for quite a while. At Berklee, some professors introduced us to these for the purpose of little Theremin projects, MIDI controllers, or any other digital music application that can utilize hand movement in a creative way.

In the AR/VR world, these have been rigged up to be mounted on the front of an HMD with the assumption that your hands could replace handheld controllers. However with the somewhat recent increase of XR devices that utilize inside-out tracking, the necessity of a separate third-party camera attachment is redundant, as the cameras required to achieve inside-out tracking can be used to track the user’s hands as well as the surrounding environment. Long story short, while these devices are functional and handy (sorry), their use-cases are limited and often more of a hassle to use in an industrial setting than they’re worth.

*Until* I finally had the mental bandwidth and free time one afternoon to bring one of my silly ideas for this device to reality. I can’t remember exactly what gave me this idea, and it’s a pretty simple one. Maybe watching Tony Stark throw holographic windows and 3D models around his office… who knows.

## Concept

Adjusting my desktop speakers’ volume is awkward. My audio interface is an under-utilized Zoom F8, which has a teeny tiny little output volume knob with crazy high resistance, so I have to either squeeze my lanky hands under my monitor to turn it without pushing my interface off my desk, or reach over to my stereo amplifier that receives the analog output signal, but that’s a stretch, literally. The obvious workaround is just to turn my Windows system volume up and down with my mouse, or my keyboard’s function buttons (not a fan). Enter my little Leap Motion controller, Unity, and the ever-helpful and well-documented resource: MRTK.

What I wanted was to just change Windows’ system volume with the wave of my hand.

## Adjusting the Volume

First, I had to find out if the functionality of setting Windows volume via a third-party program was ‘allowed.’

As usual, I wasn’t the first one to ask this question, as a quick Google search yielded exactly what I needed thanks to some folks smarter than me, on the one true programming god’s domain, StackExchange.

Okay great. Now I can set the system volume from Unity via C# methods.

## Leap Motion in Unity

I won’t spend a bunch of time here, as this is pretty routine stuff. Basically, I just followed the MRTK docs step-by-step to get MRTK and the Leap Motion plugin to play nice.

After bit of tinkering and playing around with the MRTK resources and prefabs, I decided their implementation of a pinchable slider was suitable for my needs.

From there I just made a simple script to act as the middleman between the MRTK slider and the VolumeManager script.

You can see the initial implementation [here](https://www.instagram.com/p/CI_1sEVn5_9/?ig_rid=787b1ef9-9dc7-4d57-950f-7df59769a664).

## Practical Visual Feedback

Obviously that doesn’t look great. It works just fine if I leave it running in the background, but I’m not happy looking at that. So that brought up an interesting idea: I’m already using dll function calls for the system volume control… could I wire up some C++ functionality to draw a graphic overlay to display a volume slider? Maybe something similar to the popup display that Windows gives you when you adjust the volume via function buttons on the top right corner of your display?

Enter, my hero of the day… Code Monkey. In this video, he describes step-by-step how to draw a transparent, always-on-top interface in Unity using native plugin calls. After finding exactly what I needed before with the system volume control plugin code up above, watching this video explain exactly what I needed to know and answer every question I had… it was a little surreal. I’ve barely even done anything on this project, I just kinda smashed a few toys together and here we are…

Anyways, with that incredibly handy new information, I quickly hooked up a basic native Unity slider UI that fades in when your hand is detected by the controller, and fades out 3 seconds after it loses my hand. Adjust the look a bit and I’ve got the next iteration of my interface:

<iframe width="700" height="394" src="https://www.youtube.com/embed/8O4_sYaogAI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For now, I’m content to leave it in this state as it suits my needs perfectly, though there are a few little UX improvements I plan to update some time when I feel motivated to do so. I’ll probably make this little tool public on GitHub for anyone to use and edit to suit their own preferences, so if you’re eager to try it out for yourself, message me if I’m being slow in updating this post!