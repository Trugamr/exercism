export class ResistorColor {
  private colors: string[];
  private colorMap: {
    [key: string]: number;
  } = {
    black: 0,
    brown: 1,
    red: 2,
    orange: 3,
    yellow: 4,
    green: 5,
    blue: 6,
    violet: 7,
    grey: 8,
    white: 9,
  };

  constructor(colors: string[]) {
    if (colors.length < 2) throw "At least two colors need to be present";
    this.colors = colors.slice(0, 2);
  }
  value = (): number => {
    const digits: number[] = this.colors.map(
      (color: string) => this.colorMap[color]
    );
    return parseInt(digits.join(""));
  };
}
