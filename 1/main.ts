import { readFileSync } from "fs";

function zip<T1, T2>(a: Array<T1>, b: Array<T2>): Array<[T1, T2]> {
    return a.slice(0, Math.min(a.length, b.length))
        .map((val, idx) => [val, b[idx]]);
}

function parse(path: string): Array<[number, number]> {
    return readFileSync(path, 'utf-8')
        .split("\n")
        .map((x) => x.replace('   ', ','))
        .map((x) => x.split(','))
        .map(([x, y]) => [parseInt(x, 10), parseInt(y, 10)]);
}

function sortLocations(locations: Array<[number, number]>): [number[], number[]] {
    return [
        locations.map((x) => x[0]).sort((n1, n2) => n1 - n2),
        locations.map((x) => x[1]).sort((n1, n2) => n1 - n2)
    ];
}

function getDistanceSum(locations: [number, number][]): number {
    return locations.reduce<[number[], number]>(
        (acc, x) => {
            const diff = Math.abs(x[0] - x[1]);
            return [[...acc[0], diff], acc[1] + diff];
        },
        [[], 0]
    )[1];
}

function transposeLocations(input: number[][]): number[][] {
    return input[0].map((_, columnIndex) =>
        input.map(row => row[columnIndex])
    );
}

function solvePartOne(data: Array<[number, number]>): number {
    let [left, right] = sortLocations(data);
    let zipped = zip<number, number>(left, right);
    let distSum = getDistanceSum(zipped);
    return distSum;
}

function solvePartTwo(data: Array<[number, number]>): number {
    let counter: Map<number, number> = new Map();
    let [leftLocs, rightLocs]: number[][] = transposeLocations(data);

    // make a frequency counter for right locations
    rightLocs.forEach(key => {
        counter.set(key, (counter.get(key) || 0) + 1);
    });

    // count similarity score based on freq counter 
    return leftLocs.reduce<number>(
        (acc, loc) => {
            const val = (counter.get(loc) || 0) * loc;
            return acc + val;
        },
        0
    );
}

const locationData: [number, number][] = parse('./input.txt')
console.log("part one: ", solvePartOne(locationData));
console.log("part two: ", solvePartTwo(locationData));    