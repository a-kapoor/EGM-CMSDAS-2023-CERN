# Import libraries
import numpy as np
import matplotlib.pyplot as plt

def generate_random_numbers(x0, gamma,n):
    """Generate random numbers from Breit-Wigner distribution"""
    # Generate uniform random numbers between 0 and 1
    uniform_numbers = np.random.uniform(0, 1, n)

    # Transform uniform numbers to Breit-Wigner distribution
    breit_wigner_numbers = np.tan(np.pi * (uniform_numbers - 0.5))

    # Scale and shift the numbers to match desired x0 and gamma values
    breit_wigner_numbers = x0 + gamma * breit_wigner_numbers

    return breit_wigner_numbers

# Define a function to generate electron pairs with a realistic invariant mass
def generate_electron_pairs_with_mass(n, mean=91, std=2.5):
    # Set the seed for reproducibility
    np.random.seed(42)
    # Generate random m_ee values from a normal distribution with given mean and std
    #m_ee = np.random.normal(mean, std, n)
    m_ee = generate_random_numbers(mean, std, n)
    # Convert m_ee from GeV to MeV
    m_ee = m_ee * 1000
    # Generate random eta values between -5 and 5
    eta1 = np.random.uniform(-5, 5, n)
    eta2 = np.random.uniform(-5, 5, n)
    # Generate random phi values between 0 and 2*pi
    phi1 = np.random.uniform(0, 2*np.pi, n)
    phi2 = np.random.uniform(0, 2*np.pi, n)
    # Calculate the pT values using the inverse of the formula for the invariant mass
    pT1 = np.sqrt(m_ee**2 / (2 * (np.cosh(eta1 - eta2) - np.cos(phi1 - phi2))))
    pT2 = pT1 # The pT values are equal by symmetry
    # Return a tuple of arrays
    return (pT1, pT2, eta1, eta2, phi1, phi2)

# Define a function to calculate the di-electron invariant mass
def calculate_invariant_mass(pT1, pT2, eta1, eta2, phi1, phi2):
    # Convert pT from GeV to MeV
    pT1 = pT1
    pT2 = pT2
    # Calculate the invariant mass using the formula
    m_ee = np.sqrt(2*pT1*pT2*(np.cosh(eta1 - eta2) - np.cos(phi1 - phi2)))
    # Return the invariant mass array
    return m_ee

def reco_electron_pairs(pT1, pT2, eta1, eta2, phi1, phi2,calib):
    recopT1=pT1*(calib-0.05)
    recopT2=pT2*(calib-0.05)
    
    recoeta1=eta1
    recoeta2=eta2
    
    recophi1=phi1
    recophi2=phi2
    
    return recopT1,recopT2,recoeta1,recoeta2,recophi1,recophi2