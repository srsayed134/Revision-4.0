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