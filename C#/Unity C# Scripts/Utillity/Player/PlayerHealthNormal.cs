using UnityEngine;
using UnityEngine.Audio;
using System.Collections;
using TMPro;

public class PlayerHealthNormal : MonoBehaviour
{
    [Header("Main Health")]
    public int maxHealth = 10;
    public int currentHealth;
    public GameObject HealthSlider;
    public TMP_Text healthText;

    [Header("Player")]
    public GameObject playerBody;
    Vector3 current;

    void Start()
    {
        currentHealth = maxHealth;  
    }

    private void Update() 
    {
        if(currentHealth <= 0)
        {
            current = playerBody.transform.position;
            playerBody.GetComponent<PlayerMovement>().enabled = false;
        }
    }

    public void TakeDamage(int amount)
    {
        currentHealth -= amount;
        if(currentHealth <= 0)
        {
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
