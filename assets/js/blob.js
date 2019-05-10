let weights = new Array(21).fill(0);
const r = 20;
const blob = document.querySelector('#personalBlob');

function hashCode(s) {
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        weights[j] += s.charCodeAt(i);
        j++;
        if (j >= weights.length) {
            j = 0;
        }
    }
    // Normalizing values
    const ratio = Math.max.apply(Math, weights);
    weights = weights.map(function (v, index) {
        return v / ratio * r + index;
    });
}

function calculateParallelPoint(startX, startY, x, y) {
    let v = [(startX - x), (startY - y)];
    return [(startX + v[0]), (startY + v[1])];
}

function generateNewBlob() {
    // Start point
    let startX = 82 + weights[0] / 2;
    let startY = 22 + weights[1] / 3;

    // Point 2
    let p2c1x = 120 + weights[2];
    let p2c1y = 20 + weights[3];

    // Point 6
    let p6cx, p6cy;
    [p6cx, p6cy] = calculateParallelPoint(startX, startY, p2c1x, p2c1y);

    let d = `M ${startX} ${startY}
    C ${p2c1x} ${p2c1y}, ${136 + weights[4]} ${30 + weights[5]}, ${145 + weights[6]} ${54 + weights[7]}
    S ${156 + weights[8]} ${94 + weights[9]}, ${132 + weights[10]} ${115 + weights[11]} 
    S ${83 + weights[12]} ${144 + weights[13]}, ${57 + weights[14]} ${124 + weights[15]} 
    S ${16 + weights[16]} ${81 + weights[17]}, ${34 + weights[18]} ${54 + weights[19]} 
    S ${p6cx} ${p6cy}, ${startX} ${startY}`;

    let tween = KUTE.to('#personalBlob',
        {
            path: d
        },
        {
            duration: 800,
            easing: 'easingElasticOut',
            morphPrecision: 3
        }
    ).start();
    document.querySelector('#personalBlob').setAttribute('d', d);
}

generateNewBlob(Math.random() * 20);