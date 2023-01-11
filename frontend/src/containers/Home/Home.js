import React from 'react';
import { Typography } from '@material-ui/core';
import CSVReader from 'react-csv-reader';

class Home extends React.Component {
	constructor(props) {
		super(props);
		this.state = {};
	}
	render() {
		const papaparseOptions = {
			header: true,
			dynamicTyping: true,
			skipEmptyLines: true,
			transformHeader: (header) =>
				header.toLowerCase().replace(/\W/g, '_'),
		};
		const uploadCSV = () => {
			const csvContent = document.getElementById('csv-content');
			document.getElementById('react-csv-reader-input').click();
		};
		const handleForce = (data, file_info) => {
			console.log(data, file_info);
			this.setState(file_info);
		};

		return (
			<>
				<Typography variant="h5">CSV Reader</Typography>
				<div
					className="upload-container"
					id="csv-content"
					onClick={uploadCSV}
				>
					{this.state.name ? this.state.name : 'Upload CSV '}
				</div>
				<CSVReader
					cssClass="react-csv-input"
					label="Select CSV with secret Death Star statistics"
					onFileLoaded={handleForce}
					parserOptions={papaparseOptions}
				/>
			</>
		);
	}
}

export default Home;
