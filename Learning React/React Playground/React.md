# React

> If you don't know what DOM is click [here](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) and if you are oblivious what XML is (like I was at first) click [here](https://www.w3schools.com/xml/xml_whatis.asp).
>
> Resource of this knowledge comes from.... [facebook/**create-react-app**  ](https://github.com/facebook/create-react-app) and [React Documentation](https://reactjs.org/docs/introducing-jsx.html).

## Creating your App!

When running these commands you may need to use `sudo`, meaning, you will need to add `sudo` in front of the given commands. This installation may take a few minutes to fully create the app.

### npx (it comes with npm 5.2+)

```bash
npx create-react-app my-app
```

### npm

```bash
npm init react-app my-app
```

### yarn

```bash
yarn create react-app my-app
```

## Run your Project!

Before running these commands change your directory to your app root directory

 `cd <your-app-dir>` ; your project will run in development mode.

### npm

```bash
npm start
```

### yarn 

```bash
yarn start
```

>`npm test` and `yarn test` allows you run the project in an interactive mode.

## Build your Project!

These commands will build the project to the `build` folder. After it is build your app is ready for deployment.

### npm

```bash
npm build
```

### yarn 

```bash
yarn build
```

## JSX [<u>J</u>ava<u>S</u>cript <u>X</u>ML]

> JSX is closely related to JS so use the same naming conventions when using it. (camelCase)

### The Basics

```react
const example = <p>Helloooooooo</p>
```

What the hell is this? It is called JSX. Is it JavaScript with HTML? Yes, it is but it is an extension to the JS syntax, and JSX produces React elements. 

The goal of JSX is to avoid the high coupling that is so prevalent in UI technologies, instead of, having markup and logic in separate files por que no los dos? 

#### Embedding the JSX

```react
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

You can insert JSX into the markup by placing the JSX variable in `{}`. You can place any valid JavaScript expression within those curly braces.

After compilation JSX turns into regular JS, meaning, you can place JSX as function arguments, for, if statements, return it from functions, and of course assigning it to variables.

```react
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```

#### Attributes and JSX

You can wrap string literals in double quotes to set as attributes.

```react
const element = <div tabIndex="0"></div>;
```

OR you can use curly braces to embed a JS expression as an attribute.

```react
const element = <img src={user.avatarUrl}></img>;
```

#### Children in JSX

When a tag is empty you can immediately close it after the attribute using `/>`.

```react
const element = <img src={user.avatarUrl} />;
```

JSX can have children

```react
const element = (
	<div>
		<h1> Hello, {anem} thanks for reading me again!</h1>
	</div>
);
```

#### JSX Kind of Prevents Injections

React DOM automatically escapes input given to JSX before rendering it.

```react
const title = response.potentiallyMaliciousInput;
// This is safe:
const element = <h1>{title}</h1>;
```

#### JSX and Objects

Babel compiles JSX to `React.createElement()` calls

The examples are the same

```react
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```

```react
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

`React.createElement()`  performs a few checks to make sure the code is bug-free, and the end it creates an object like this:

```react
// Note: this structure is simplified
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
  }
};
```

The objects are called **React Elements** and what is; it shows the what you see on the screen. React reads these objects and constructs it to create the DOM.

## Rendering Elements

Elements shows what it is on the screen.

```react
const element = <h1>Hello, world</h1>;
```

React elements are plain objects, making it cost efficient.

### Rendering into the DOM

The is a `<div>` somewhere within the HTML file...

```react
<div id="root"></div>
```

This is called the root DOM node because everything within this `<div>` will be maintained by the React DOM.

If you are creating the app with solely React, you can built the whole React project within this `<div>` but if you are embedding React you can have many instances of this node throughout your project.

To render the React element to the DOM you have to use `ReactDOM.render()`...

```react
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

### Changing Already Rendered Elements

In React, the elements that are rendered to the DOM are immutable.  To update a rendered element you can the update can be triggered by an event or by simply using time function.

```react
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}

setInterval(tick, 1000);
```

DOM only updates what is necessary so it compares the children to the previous one and only updates changes.

## Components and Props

### Function and Class Components

A function similar to...

```react
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

This a valid React component because it accepts one props and uses one prop, prop being properties. This function returns a React element and these functions are just JS functions.

You can also use a class to define the component

```react
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

### Rendering a Component

