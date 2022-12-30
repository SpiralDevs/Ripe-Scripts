using UnityEngine;
using UnityEngine.Audio;
using System.Collections;
using TMPro; // or if you don't use text mesh pro, use "using UnityEngine.UI;"

public class PlayerHealth : MonoBehaviour
{
    [Header("Main Health")]
    public int maxHealth = 10;
    public int currentHealth;
    public GameObject HealthSlider;
    public TMP_Text healthText; // if you are using the defeault unity engine ui, use "public Text healthText;" otherwise forget about this 

    [Header("Player")]
    public GameObject playerBody;
    Vector3 current;

    public bool isBroDead; // don't really need this but if you want to test using this go ahead
    
    [Header("Menus")]
    public GameObject deathMenu;
    public GameObject winMenu;


    void Start()
    {
        currentHealth = 10;  
        deathMenu.SetActive(false);
        winMenu.SetActive(false);
    }

    private void Update() 
    {

        if(currentHealth <= 0)
        {
            isBroDead = true;
            deathMenu.SetActive(true);
            current = playerBody.transform.position;
            playerBody.GetComponent<PlayerMovement>().enabled = false;
        }
    }

    public void TakeDamage(int amount)
    {
        currentHealth -= amount;
        if(currentHealth <= 0)
        {
            isBroDead = true;
            deathMenu.SetActive(true);
            current = playerBody.transform.position;
            playerBody.GetComponent<PlayerMovement>().enabled = false;
        }
    }

    public void Heal(int amount)
    {
        currentHealth += amount;
        if(currentHealth > maxHealth)
        {
            currentHealth = maxHealth;
        }
    }

}
