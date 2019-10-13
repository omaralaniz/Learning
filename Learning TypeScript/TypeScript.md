# Grasping TypeScript

## What is TypeScript

It is a superset of JavaScript made by Microsoft, and it is compiled into plain JS; meaning it can be embedded in JS projects.

### The purpose

TypeScript allows for explicit data type declaration with variables, parameter and functions, and better utilities Classes in JavaScript.

TypeScript Types

```typescript
String	  Any
Number	  Void
Boolean	  Null
Array	  Tuple
Any	  Enum
Generics
```
Class Based Objects, allows for no Prototypes, encapsulation, inherit, modifiers, and OOP.

#### Type Annotations

You can explicitly declare variables with types. For example, this little function taken from the Typescript Documentation

``` typescript
function greeter(person: string) {
    return "Hello, " + person;
}

let user = [0, 1, 2];

document.body.innerHTML = greeter(user);
```

Function `greeter` takes a parameter `person` of type string, and it is explicitly declared by `:string`. This snippet of code will throw an error because `greeter(user)` is passing `Number[]` as an argument, which, as you should know it is not a string-- hopefully...

#### Interfaces

One beautiful thing about typescript is the ability to use `interface`. Here is the use of said interface, again, taken from the official docs.

```typescript
interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}

let user = { firstName: "Jane", lastName: "User" };

document.body.innerHTML = greeter(user);
```

`interface person` has two variables `firtName` and `lastName` both type `string`. The function that implements the interface does not need a to use the explicit `implements`. You are just required to have the same shape as the interface.

#### Classes

Since, Typescript is JavaScript (extension) it allows the usage of object-oriented programming using `class`. In Typescript `interface` and `class` play nicely with one another. `Constructor` initializes the variables that the `class` will have, and those variables can be set as `public` 

```typescript
class Student {
    fullName: string;
    constructor(public firstName: string, public middleInitial: string, public lastName: string) {
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
}

interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}

let user = new Student("Jane", "M.", "User");

document.body.innerHTML = greeter(user);
```





### TypeScript Compiler

Compiles `.ts` files to `.js` and it can be installed using NPM.

## Installing TypeScript



