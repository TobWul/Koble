// <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">
//   <path d="
//   M 165 116
//   C 190 111, 246 108, 269 139
//   S 288 228, 227 242
//   S 137 240, 130 200
//   S , 165 116" stroke="black" fill="#0093bc"/>
// </svg>
//

function hashString(s) {
    let stringNum = 0;
    for (let i = 0; i < s.length; i++) {
        stringNum += parseInt(s.charCodeAt(i)) * i;
    }
    return stringNum;
}

hashString("Tobias Wulvik");

function generateNewBlob(k) {
    // Start point
    const startX = 165;
    const startY = 116;

    // Point 2
    const p2c1x = 190;
    const p2c1y = 111;
    const p2c2x = 246;
    const p2c2y = 108;
    const p2x = 269;
    const p2y = 139;


    // Point 3
    const p3cx = 288;
    const p3cy = 228;
    const p3x = 227;
    const p3y = 242;

    // Point 4
    const p4cx = 137;
    const p4cy = 240;
    const p4x = 130;
    const p4y = 200;

    // Point 5
    const p5cx = 115;
    const p5cy = 126;
    const p5x = 165;
    const p5y = 116;

    return `M ${startX} ${startY} C ${p2c1x} ${p2c1y}, ${p2c2x} ${p2c2y}, ${p2x} ${p2y} S ${p3cx} ${p3cy}, ${p3x} ${p3y} S ${p4cx} ${p4cy}, ${p4x} ${p4y} S ${p5cx} ${p5cy}, ${p5x} ${p5y}`
}

document.querySelector('#personalBlob').setAttribute('d', generateNewBlob(12));