{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf200
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww13900\viewh16280\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Bacteria-Evolutionary-NN\
\
This is my second attempt at an evolutionary neural net, building off my Food-Seeking Ant model.\
\
In this model, I intend to make bacterial that evolve to find food. As they reproduce, their neural structure will evolve, and as their numbers grow, they will have to compete with one another to survive. \
\
There are 2 major differences between this model and my previous attempt. \
\
The first is that this model will have a fluid neural structure. While my ants had a preset number of neurons in certain layers, the bacteria will start with almost nothing at all! Aside from input and output neurons, there won't even be any connections. These will evolve over time, which will hopefully lead to more interesting structures over time. This has an unintended bonus of being faster to compute at first, as there will be a single bacteria with very basic neural structure, although it would worsen with time. \
\
The second change is that the selective process will be changed drastically. Previously I was simulating 100 ants, and when they all died I took the top 10 and passed on their genes. This time, however, I intend to have almost no selective processes. Ants will compete with one another for resources, and the best will survive. This removes the idea of \'91generations\'92 from the system, and instead, different \'91species\'92 of bacteria should emerge and die out in waves. }