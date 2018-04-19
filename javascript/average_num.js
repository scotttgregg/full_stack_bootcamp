// nums = []
//
//
// while True:
//     user_input = input('Enter a number, or "done": ')
//     if user_input != 'done':
//         number = int(user_input)
//         nums.append(number)
//     elif user_input == 'done':
//         for i in range(len(nums)):
//             total = sum(nums)
//             average = total / len(nums)
//         print(average)
//         break
//     else:
//         print("not a valid option")

let nums = [];

function getSum(total, num) {
    return total + num;
}

let x = true;
while(x) {
    let user_input = prompt('Enter a number, or "done": ');
    if (user_input !== 'done') {
        let number = parseInt(user_input);
        nums.push(number);
    } else if (user_input === 'done')  {
        let i;
        for (i = 0; i < nums.length; i++) {
            let total = nums.reduce(getSum);
            x = false
        }
    }  else {
        console.log("not a valid option.")
    }
}

let average = total / nums.length;
            console.log(average)

