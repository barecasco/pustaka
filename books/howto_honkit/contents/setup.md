# HonKit Setup

To build books using HonKit you need Node.js backend engine. It has package manager called `npm` where we can install HonKit module.

## Installing Node.js

Install Node via:

https://nodejs.org/en/

Install at simplest path possible. Make sure `node` command is in the `PATH`.

## Creating HonKit Project

One has to initiate a Node project (basically a web engine) to use HonKit. After installing Node, go to the directory where you want your HonKit books reside and execute:

```
D:\> cd D:\storage\honkit
D:\storage\honkit> npm init --yes
```
You will find new folder `node_modules` which contains default Node modules for Node to be run.

There are two kinds of package in Node. The first kind is global package, whose library is recognized anywhere (directory) Node is used. The second kind is local package, whose library only recognized in corresponding directory. We want to install new HonKit module locally on the intended directory:

```
D:\storage\honkit> npm install honkit
D:\storage\honkit> npm list -depth=0
docs@1.0.0 D:\storage\honkit
+-- honkit@3.6.6
```
