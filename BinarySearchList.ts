export default function bs_list(haystack: number[], needle: number): boolean {
	let hi = haystack.length;
	let lo = 0;

    while (lo < hi) {
        const m = Math.floor(lo + (hi - lo) / 2);
        const v = haystack[m];

        if (needle === v){
            return true;
        }
        else if (needle < v){
            hi = m - 1;
        }
        else {
            lo = m + 1;
        }
    }
    return false;
}
