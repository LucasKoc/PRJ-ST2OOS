import React from 'react';
import { render, screen, waitFor, fireEvent } from '@testing-library/react';
import App from '../App';

describe('App Component', () => {
  beforeEach(() => {
    fetch.resetMocks();
  });

  test('renders the Students tab and displays data', async () => {
    fetch.mockResponseOnce(JSON.stringify([{ student_id: 20210615, first_name: 'Lucas', last_name: 'KOCOGLU' }]));

    render(<App />);

    const studentsTab = screen.getByRole('tab', { name: /Students/i });
    expect(studentsTab).toBeInTheDocument();

    expect(studentsTab).toHaveAttribute('aria-selected', 'true');

    await waitFor(() => {
      expect(screen.getByText('Lucas')).toBeInTheDocument();
    });
  });

  test('switches to Teachers tab and displays data', async () => {
    fetch.mockResponseOnce(JSON.stringify([]));

    fetch.mockResponseOnce(JSON.stringify([{ teacher_id: 'ijenhani', first_name: 'Ilyes', last_name: 'JENHANI' }]));

    render(<App />);

    const teachersTab = screen.getByRole('tab', { name: /Teachers/i });
    fireEvent.click(teachersTab);

    expect(teachersTab).toHaveAttribute('aria-selected', 'true');

    await waitFor(() => {
      expect(screen.getByText('Ilyes')).toBeInTheDocument();
    });
  });
});