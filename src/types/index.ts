export interface ChildData {
  id: string;
  age: number;
  height: number;
  weight: number;
  gender: 'boy' | 'girl';
  createdAt: string;
  updatedAt: string;
}

export interface WHOStandard {
  age: number;
  SD4neg: number;
  SD3neg: number;
  SD2neg: number;
  SD1neg: number;
  SD0: number;
  SD1: number;
  SD2: number;
  SD3: number;
  SD4: number;
}

export interface User {
  uid: string;
  email: string;
  displayName: string | null;
  photoURL: string | null;
}

export interface ChartData {
  labels: number[];
  datasets: {
    label: string;
    data: number[];
    borderColor: string;
    fill: boolean;
  }[];
}
