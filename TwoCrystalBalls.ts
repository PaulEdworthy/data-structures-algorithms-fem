export default function two_crystal_balls(breaks: boolean[]): number {

    const jump = Math.floor(Math.sqrt(breaks.length));

    // set your jump to sqrt of n
    let i = jump;

    // search jumping forwards the jump distance
    for(; i < breaks.length; i += jump) {
        if (breaks[i]) {
            break;
        }
    }

    // go back to the previous jump to search
    i -= jump;

    for (let j = 0; j < jump && i < breaks.length; i++, j++) {
        if (breaks[i]) {
            return i
        }
    }

    return -1;
}