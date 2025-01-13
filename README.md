# Child Growth Monitor

A comprehensive web application for tracking and monitoring children's growth using WHO standards and modern growth assessment techniques.

## Features

- **Growth Tracking**: Monitor height, weight, and BMI with historical trends
- **WHO Standards Integration**: Compare measurements against WHO Child Growth Standards
- **Interactive Visualizations**: Dynamic growth charts and trend analysis
- **Individual Child Profiles**: Detailed profiles with growth history and status
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## Growth Assessment Methods

### Height/Length Measurement

#### For Children Under 2 Years
- **Recumbent Length**: Measured lying down
- Required Equipment: Length board with fixed headpiece and movable footpiece
- Precision: Measurements recorded to nearest 0.1 cm
- Two people required for accurate measurement

#### For Children 2 Years and Older
- **Standing Height**: Measured standing upright
- Required Equipment: Stadiometer or height board
- Precision: Measurements recorded to nearest 0.1 cm
- Child should stand with:
  - Heels together
  - Shoulders level
  - Head in Frankfurt plane position

### Weight Measurement

- **Equipment**: Electronic scale with 0.1 kg precision
- **Procedure**: 
  - Zero scale before each measurement
  - Child wearing light clothing only
  - Record to nearest 0.1 kg

### Growth Standards Reference

We use the WHO Child Growth Standards (0-5 years) and WHO Growth Reference (5-19 years):

#### Key Indicators
- Length/height-for-age
- Weight-for-age
- Weight-for-length/height
- Body mass index (BMI)-for-age

#### Z-Score Classifications
- Above 3: Severely high
- Above 2: High
- 0: Median
- Below -2: Low
- Below -3: Severely low

## Technical Implementation

### Growth Chart Calculations

```typescript
interface GrowthData {
  age: number;        // Age in months
  measurement: number; // Height or weight
  zscore: number;     // Standard deviation from median
}

// Z-score calculation
const calculateZScore = (measurement: number, median: number, sd: number): number => {
  return (measurement - median) / sd;
};

// Growth velocity calculation (cm/month)
const calculateGrowthVelocity = (
  currentHeight: number,
  previousHeight: number,
  monthsDifference: number
): number => {
  return (currentHeight - previousHeight) / monthsDifference;
};
```

### WHO Data Integration

We use the following WHO growth chart data:
- `who-growth-standards.json`: Contains median and SD values for different ages
- Growth charts are generated using `react-chartjs-2`
- Data is interpolated for precise age-based calculations

## Getting Started

### Prerequisites

- Node.js >= 16.0.0
- npm >= 7.0.0
- Firebase account for data storage

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/child-growth-monitor.git
cd child-growth-monitor
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
# Edit .env.local with your Firebase credentials
```

4. Run the development server:
```bash
npm run dev
```

## References

1. WHO Child Growth Standards: [WHO Website](https://www.who.int/tools/child-growth-standards)
2. de Onis M, et al. [Development of a WHO growth reference for school-aged children and adolescents](https://pubmed.ncbi.nlm.nih.gov/18026621/)
3. WHO Multicentre Growth Reference Study Group. [WHO Child Growth Standards: Length/height-for-age, weight-for-age, weight-for-length, weight-for-height and body mass index-for-age: Methods and development](https://www.who.int/publications/i/item/924154693X)

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- World Health Organization for growth standards data
- React and Next.js communities
- All contributors and maintainers
