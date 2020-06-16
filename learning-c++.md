---
description: A documentation of my learning journey of C++
---

# Learning C++

I have decided, during this period of lockdown due to COVID-19, to learn some C++. Being a maths graduate, I usually tampered with high-end languages and didn't go any lower than something like PHP. This is a shame, since learning middle or lower level languages can improve understanding of lower level concepts that are important, such as memory allocation. C++ is a middle level language and a good place for me to start.

{% hint style="info" %}
This is not a tutorial for C++ but simply an account of my learning. I used the tutorial from Tutorialspoint available [here](https://www.tutorialspoint.com/cplusplus/) to learn C++ and what is written here, either comes from, or is motivated by, this tutorial.
{% endhint %}

### Basic Notions

There are some important things to clear up before I start writing my first C++ program. Here are the distinctions between Objects, Classes, Methods and Instance Variables.

* **Object** − Objects have states and behaviors. Example: A dog has states - color, name, breed as well as behaviors - wagging, barking, eating. An object is an instance of a class.
* **Class** − A class can be defined as a template/blueprint that describes the behaviors/states that object of its type support.
* **Methods** − A method is basically a behavior. A class can contain many methods. It is in methods where the logics are written, data is manipulated and all the actions are executed.
* **Instance Variables** − Each object has its unique set of instance variables. An object's state is created by the values assigned to these instance variables.

### Hello World

As always, my first C++ program is just Hello World.

```cpp
#include <iostream>

using namespace std;

// Begin program execution
int main() {
    cout << "Hello World";

    return 0;
}
```

The main things to notice are that C++ uses a `;` to terminate statements, it encloses function code in `{}` which represent blocks and it requires declaring a variable type at the time of variable declaration.

{% hint style="warning" %}
C++ is case sensitive and identifiers \(of variables, functions etc.\) must start with a letter or an underscore and can contain any number of subsequent letters, underscores or numbers. Like other languages, C++ has some reserved keywords that cannot be used as names, these can be found [here](https://www.tutorialspoint.com/cplusplus/cpp_basic_syntax.htm).
{% endhint %}

### Data Types

C++ contains a number of primitive data types that are as follows:

| Type | Keyword |
| :---: | :---: |
| Boolean | bool |
| Character | char |
| Integer | int |
| Floating Point | float |
| Double Floating Point | double |
| Valueless | void |
| Wide Character | wchar\_t |

These primitive data types can be modified using the prefixes signed, unsigned, short or long to make other data types. These do as they say, unsigned makes a number non-negative and long/short changes the length of a number.

The size of a data type can be determined using the `sizeof()` function applied to a data type.

#### Creating New Data Types

New data types can be created using `typedef type name`. For example, to define a new type called whale we can use the following code:

```cpp
typedef string whale;
whale Betty "My name is Betty and I am a whale";
```

Which defines a whale named Betty with the given string value.

Enumeration data types can also be created using the `enum` keyword:

```cpp
enum whale {small, medium, large = 3} w;
w = medium;
```

Here the value of the first name is 0, the second 1, etc. Though we can assign specific values to a name, like we have with `large = 3`.

### Variable Types

The basic variable types are, unsuprisingy, the same as those for the data types. We define variables by indicating their type followed by their name. Multiple variables can be instantiated at the same time and a value may or may not be asigned. For example:

```cpp
int a = 3;
float a,b,c;
char z, x = 'x';

```

Where variables are defined without an initial value, they take the value NULL with all bytes set to 0.

