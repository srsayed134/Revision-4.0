// Example of DSA ++++++++++++++

//This is data structure
/*
const studentsDatabase = ["Jordan", "Erick", "Jhon","Michel"];
//This is algorithm to found specific data
const findStudent = (allStudent, studentName) => {
    for(let i = 0; i < allStudent.length; i++){
        if(allStudent[i] === studentName){
            console.log(`${studentName} found`)
            return;
        }
    }
    console.log(`${studentName} is not found`)
}
findStudent(studentsDatabase, "Sayed")
*/
// Big O notation +++++++++++++
//BigO notation helps us understand how long an algorithm will 
// take to run or how much memory it will need as ther amount of data 
// it handles grows

//O(n)
// Signifies that the execution time of the algorithm grows linearly 
// in proportion to the size of the input data (n)

// Example  of O(n)
/*
const groceries = ["Milk", "Bread", "Egg", "Oil", "Icecreame", "Suger"];

const findProdunct = (groceriesitem, item) => {
    for(let i = 0; i < groceriesitem.length; i++){
        if(groceries[i] === item){
            console.log(`${item} is found`)
        }
    }
    //Example of O(2n) but O(n)
    for(let j = 0; j< groceriesitem.length; j++){
        if(groceriesitem[j] === item){
            console.log(`${item} also found`)
        }
    }
    // n + n = 2n
    //Drop the constant so it becomes O(n)
}

findProdunct(groceries, "Egg")
*/

// Example of O(1) ++++++++++++++
//(Imagine you have a box filled with items, and you know exectly where each item is located. To get a specific item, you go directly to its location, taking the same amount of time irrespective of how many items are in the box)
/*
const number = [1,2,3,4,5];
const getElement = (arr, index) => arr[index];

console.log(getElement(number, 2));
*/
//We know the position of index of number

// O(n^2) +++++++++++++++++++++++++
// (Imagine you have a box of items and want to comare each item with every other item to find specific pairs. As the number of items (n) increases, the number of comparisons (n^2) grows much faster)
/*
function findPairs(arr){
    for (let i = 0; i <arr.length; i++){
        for (let j = i + 1; j <arr.length; j++){
            console.log(`Pair: ${arr[i]} ${arr[j]}`)
        }
    }
}

const numbers = [1,2,3,4,5];
findPairs(numbers)
*/

//O(log n) +++++++++++++++++
//O(log n) time complexity refers to an algorithms runtime that grow logarithmically with the size of the input (represented by n).In simpler terms, as the input size increases, the time it takes for the algorithm to run increases slowly

//DSA Arrays ++++++++++++++++++
//Data structure array is an ordered collection of elements that can be accessed using a numerical index
class MyArray {
    constructor() {
        this.length = 0;
        this.data = {}
    }
    push(item){
        this.data[this.length] = item;
        this.length++
        return this.length
    }
    get(index){
       let find = this.data[index]
       return find
    }
    pop(){
       const lastItem = this.data[this.length -1]
       delete this.data[this.length - 1]
       this.length --
       return lastItem
    }
    shift(){
        let firstItem = this.data[0]
        //Reindexing
        for(let i = 0; i < this.length; i++){
            this.data[i] = this.data[i + 1]
        }
        //Delete last length
        delete this.data[this.length - 1] //This last data should have removed because last length is created with out data
        this.length--
        return firstItem

    }
    delete(index){
        let item = this.data[index];
        for(let i = index; i < this.length - 1; i++){  //let i = index; i < this.length - 1; i++ and let i = index; i < this.length; i++ will give same result but -1 remove one unneccessary assignment

            this.data[i] = this.data[i + 1] 
        }
        delete this.data[this.length - 1]
        this.length --
        return item
    }
    unshift(item){
        this.length++
        for(let i = this.length - 1; i > 0; i--){
            this.data[i] = this.data[i - 1]
        }
        this.data[0] = item;
        return this.length
    }
}

const myNewArray = new MyArray()
myNewArray.push("Mango")
myNewArray.push("Banana")
myNewArray.push("Orange")
myNewArray.push("Pineapple")
// console.log(myNewArray)
// console.log(myNewArray.get(2))
// console.log(myNewArray.pop())
// console.log(myNewArray)
// console.log(myNewArray.shift())
// console.log(myNewArray)
// myNewArray.delete(2)
console.log(myNewArray)
myNewArray.unshift("Watermelon")
console.log(myNewArray)