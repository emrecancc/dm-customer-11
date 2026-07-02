import React from 'react';
import { render } from '@testing-library/react';
import Dashboard from '../Dashboard';

describe('Dashboard', () => {
  it('renders correctly', () => {
    // Mock the current date to a fixed value to make the snapshot deterministic
    jest.useFakeTimers('modern');
    jest.setSystemTime(new Date('2024-01-14'));

    const { container } = render(<Dashboard />);
    expect(container).toMatchSnapshot();
  });
});